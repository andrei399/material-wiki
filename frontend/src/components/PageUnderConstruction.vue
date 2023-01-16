<template>
    <v-card rounded="lg" width="90%" class="mx-auto mt-3 mb-3 orange" elevation="3" v-if="image_data">
        <v-card-text bold>
            <v-row cols="10" align="center">
                <v-col sm="1" align="left" v-if="image_data.image">
                    <v-img sm="1" :src="image_data.image" :title="image_data.name" width="50" height="50" />
                </v-col>
                <v-col align="center" sm="10">
                    <h4 align="center">"I shall organize, see to everything and whip the house into order"</h4>
                </v-col>
                <v-col align="right" v-if="image_data.image">
                    <v-img sm="1" :src="image_data.image" :title="image_data.name" width="50" height="50" />
                </v-col>
            </v-row>
        </v-card-text>
        <v-card-text align="center">
            This article is currently under construction for major revisions. We ask that edits to this article are only minor or grammatical in nature until this warning is removed in order to not disrupt the major revamp. Should you have any questions regarding the revamp, consult the talk page for more info.
        </v-card-text>
    </v-card>
</template>

<script>
export default {
    name: 'PageUnderConstruction',
    setup() {
        return {}
    },
    data() {
        return {
            image_data: null,
        }
    },
    async created(){
        var req_data = await this.$axios.get('http://localhost:8000/api/img/UNDER%20CONSTRUCTION/').catch().then(response => response.data)
        this.image_data = req_data
    },
}
</script>