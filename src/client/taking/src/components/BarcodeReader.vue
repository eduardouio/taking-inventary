<template>
    <div class="row bg-success">
         <div id="result_strip">
            <ul class="thumbnails"></ul>
            <ul class="collector"></ul>
          </div>
          <div id="interactive" class="viewport"></div>
        <div class="col mt-1">
            <video id="video"></video>
            <canvas id="canvas"></canvas>
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
        const canvas = document.querySelector('#canvas');
        const ctx = canvas.getContext('2d');

        // Configurar Quagga
        Quagga.init({
            inputStream: {
                name: 'Live',
                type: 'LiveStream',
                target: canvas,
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
        });

        // Capturar el código de barras cuando se detecte
        Quagga.onDetected(function (result) {
            console.log(result.codeResult.code);
            self.ean_code(result.codeResult.code);

            // mostrar captura de video
            var code = result.codeResult.code;
            var $node = null, canvas = Quagga.canvas.dom.image;
            $node = $('<li><div class="thumbnail"><div class="imgWrapper"><img /></div><div class="caption"><h4 class="code"></h4></div></div></li>');
            $node.find("img").attr("src", canvas.toDataURL());
            $node.find("h4.code").html(code);
            $("#result_strip ul.thumbnails").prepend($node);
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
            this.$emit('ean_code', code);
        },
        stop() {
            Quagga.stop();
        },
    },
    beforeDestroy() {
        // Detener la captura de video cuando se destruye el componente
        Quagga.stop();
    },
};
</script>
