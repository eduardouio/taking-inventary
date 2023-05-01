<template>
    <div class="row">
        <div class="col mt-1">
            <video id="video" class="img-fluid"></video>
        </div>
    </div>
</template>

<script>
import Quagga from 'quagga';

export default {
    name: 'BarcodeReader',
    emits: ['ean_code'],
    mounted() {
        // Obtener referencias a los elementos de video y canvas
        const self = this;
        const video = document.querySelector('#video');

        // Configurar Quagga
        Quagga.init({
            inputStream: {
                name: 'Live',
                type: 'LiveStream',
                target: video,
            },
            decoder: {
                readers: ['ean_reader'],
            },
        }, function (err) {
            if (err) {
                console.error('Error al inicializar Quagga:', err);
                return;
            }
            Quagga.start();
            navigator.mediaDevices.getUserMedia({ video: true })
                .then(function (stream) {
                    video.srcObject = stream;
                    video.play();
                }).catch(function (err) {
                    alert('Error al acceder a la cámara: ' + err);
                })
        });

        // Capturar el código de barras cuando se detecte
        Quagga.onDetected(function (result) {
            console.log(result.codeResult.code);
            self.ean_code(result.codeResult.code);
            Quagga.stop();
        });

        // Dibujar el resultado en el canvas
        Quagga.onProcessed(function (result) {
            const drawingCtx = Quagga.canvas.ctx.overlay;
            const drawingCanvas = Quagga.canvas.dom.overlay;

            if (result) {
                if (result.boxes) {
                    drawingCtx.clearRect(0, 0, parseInt(drawingCanvas.getAttribute('width')), parseInt(drawingCanvas.getAttribute('height')));
                    result.boxes.filter(function (box) {
                        return box !== result.box;
                    }).forEach(function (box) {
                        Quagga.ImageDebug.drawPath(box, { x: 0, y: 1 }, drawingCtx, { color: 'green', lineWidth: 2 });
                    });
                }

                if (result.box) {
                    Quagga.ImageDebug.drawPath(result.box, { x: 0, y: 1 }, drawingCtx, { color: '#00F', lineWidth: 2 });
                }

                if (result.codeResult && result.codeResult.code) {
                    Quagga.ImageDebug.drawPath(result.line, { x: 'x', y: 'y' }, drawingCtx, { color: 'red', lineWidth: 3 });
                }
            }
        });
    },
    methods: {
        ean_code(code) {
            Quagga.stop();
            this.$emit('ean_code', code);
        },
        stop() {
            Quagga.stop();
        },
    },
    beforeUnmount() {
        Quagga.stop();
    }
};
</script>
