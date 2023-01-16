<template>
    <v-card elevation="4" shaped outlined>
        <v-card-text align="center" class="mx-0">
            <v-row>
                <v-spacer class="mt-3 mb-7 bf">
                    <v-title>
                        {{ title }}
                    </v-title>
                </v-spacer>
            </v-row>
            <v-img v-if="img.image" height="200" :src=img.image :title="img.name"></v-img> <!-- noqa -->
            <v-btn v-else>
                Upload Image
            </v-btn>
            <div v-for="(item, key) in infos" :key="key">
                <v-row>
                    <v-spacer>
                        <AppCardTextSections v-if="item.type == 'text'" :item="item" class="info"/>
                        <AppCardListSections v-else-if="item.type == 'list'" :item="item" class="info"/>
                    </v-spacer>
                </v-row>
            </div>
        </v-card-text>
    </v-card>
</template>

<style scoped>
/* change font size for v-title */
.bf {
    font-size: 2rem;
}
.info{
    background-color: #616161;
    color:white;
}
</style>

<script lang="js">
import AppCardListSections from './AppCardListSections.vue'
import AppCardTextSections from './AppCardTextSections.vue'

export default ({
    name: 'AppCard',
    components: {
        AppCardListSections,
        AppCardTextSections,
    },
    setup() {
        return {}
    },
    props: {
        payload: {
            type: Object,
            required: true,
        },
        tab: {
            type: String,
            required: true,
        },
    },
    data() {
        return {
            infos: Object,
            title: String,
            img: String,
        }
    },
    async created() {
        // var data = await this.data
        // console.log(data)
        var card_data = this.payload.items.filter(item => item.name == this.tab)[0].card
        this.title = card_data.title
        this.infos = card_data.info
        this.img = card_data.image[0]
    },
})
</script>
