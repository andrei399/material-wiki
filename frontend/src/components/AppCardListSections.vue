<template>
    <v-card elevation="3" class="mt-5 mb-10" shaped outlined>
        <v-card-text align="center">
            <v-title class="title" @click="lets_go(item)">
                {{ item.title }}
            </v-title>
        </v-card-text>
        <v-column>
            <v-card-text align="center" class="text mt-2" v-for="(item, key) in item.values" :key="key">
                {{ item.value }} ce pls
            </v-card-text>
        </v-column>
    </v-card>
</template>

<style scoped>
.title {
    font-weight: 500;
    font-size: 1.3rem;
}
.text {
    font-size: 1rem;
}
</style>


<script>
// import AppCardListSingle from './AppCardListSingle.vue'


export default ({
    name: 'AppCardListSections',
    components: {
        // AppCardListSingle,
    },
    props: {
        item: {
            type: Object,
            required: true,
        },
    },
    setup(){
        return {}
    },
    created() {
        console.log(this.item)
    },
    methods: {
        lets_go(item) {
            console.log(item.values[0].values)
        }
    }
})
</script>