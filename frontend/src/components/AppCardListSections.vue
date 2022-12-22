<template>
    <v-card elevation="3" class="mt-5 mb-10" shaped outlined>
        <v-card-text align="center">
            <v-title class="title" @click="lets_go(item)">
                {{ item.title }}
            </v-title>
        </v-card-text>
        <v-column>
            <v-card-text @click="lets_go(cur_item)" class="text mt-2" v-for="(cur_item, key) in item.values" :key="key">
                <v-col align="left">
                    {{ cur_item.title }}
                </v-col>
                <v-col align="right" v-for="(value, key) in cur_item.values" :key="key">
                    <v-row>
                        {{ value }}
                    </v-row>
                </v-col>
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
    setup() {
        return {}
    },
    created() {
        console.log(this.item)
    },
    methods: {
        lets_go(item) {
            console.log(item.values)
        }
    }
})
</script>