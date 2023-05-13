<template>
   <div>
    Esta es la informacion de la empres
   </div>
</template>
<script>
export default {
    name: "EnterprisesInfo",
    data: function () {
        return {
        "data": "Genial",
        }
    },
    methods: {
        updateData: function() {
        this.data = [];
        }
    }
}
</script>

<style>

</style>