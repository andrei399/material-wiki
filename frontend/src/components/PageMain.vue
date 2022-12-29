<template>
    <div>
        <h1 align="center" @click="pula()">{{ data.big_name }}</h1>
        <page-spoilers align="center" v-if="data.spoilers" :data="data.spoilers" />
        <v-tabs v-model="tab" v-for="(value, key) in data.items" :key="key">
            <v-tab :value="value.name">{{ value.name }}</v-tab>
            <v-tab>pula</v-tab>
        </v-tabs>
        <v-window v-model="tab" v-for="(value, key) in data.items" :key="key">
            <v-window-item :value="value.name">
                <item-quote :quote="value.quote.quote" :author="value.quote.author" v-if="value.quote" />
                <v-card-text v-if="value.about" class="text">
                    {{ value.about }}
                </v-card-text>
            </v-window-item>
        </v-window>
    </div>
</template>

<style scoped>
.text {
    font-size: 1rem;
}
</style>

<script>
import PageSpoilers from './PageSpoilers.vue'
import ItemQuote from './ItemQuote.vue'

export default {

    name: 'ItemView',
    setup() {
        return {}
    },
    components: {
        PageSpoilers,
        ItemQuote,
    },
    data() {
        return {
            tab: null
        }
    },
    props: {
        data: {
            type: Object,
            required: true,
        }
    },
    methods: {
        pula() {
            console.log(this.data)
        }
    },
    computed: {
        slug() {
            return this.$route.params.slug
        },
        content() {
            console.log(this.data.data)
            return this.data.data
        }
    },

}
</script>
