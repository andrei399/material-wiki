<template >
    <v-row v-if="image_data">
        <v-card align="center" width="60%" cols="4" height="90" class="mx-auto mt-5 mb-5 orange" elevation="3" rounded="lg">
            <v-row align="center" class="mt-5">
                <v-img :src="image_data.image" :title="image_data.name" height="50" width="50"/>
                <v-card-text>
                    <v-row align="center" class="mt-10px">
                        <v-spacer />
                        <h4>"Do you really wish to know?"</h4>
                        <p>— Spoilers from the books and/or adaptations to follow! </p>
                        <v-spacer />
                    </v-row>
                </v-card-text>
                <v-img :src="image_data.image" :title="image_data.name" height="50" width="50" />
            </v-row>
        </v-card>
    </v-row>
</template>

<style>
.orange{
    border: 3px solid #d2801e;
    background-color: #616161;
    color: white;
}
</style>

<script>
export default {
    name: 'PageSpoilers',
    setup() {
        return {}
    },
    data(){
        return {
            image_data: null,
        }
    },
    async created(){
        var req_data = await this.$axios.get('http://localhost:8000/api/img/SPOILERS/').catch().then(response => response.data)
        this.image_data = req_data
    }

}
</script>
