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
            <v-img height="200" :src=img></v-img>
            <div v-for="(item, key) in infos" :key="key">
                <v-row>
                    <v-spacer>
                        <AppCardTextSections v-if="item.type == 'text'" :item="item"/>
                        <AppCardListSections v-else-if="item.type == 'list'" :item="item"/>
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
</style>

<script>
import axios from 'axios'
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
    data() {
        return {
            infos: Object,
            title: String,
            img: String,
        }
    },
    async created() {
        var data = await axios.get('http://127.0.0.1:8000/api/items/').catch(err => console.log(err))
        data = data.data
        this.title = data.title
        this.infos = data.info
        this.img = data.img
    },
    methods: {
        pula_mea(item) {
            console.log(item.type)
        }
    }
})
</script>
