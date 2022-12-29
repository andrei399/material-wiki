<template>
    <v-card elevation="3" class="mt-5 mb-1" shaped outlined>
        <v-card-text align="center" @click="expand(item)">
            <v-title class="title">
                {{ item.title }}
            </v-title>
            <div v-if="item.expandable">
                <v-icon v-if="item.expanded" align="left">mdi-chevron-down</v-icon>
                <v-icon v-else align="left">mdi-chevron-up</v-icon>
            </div>
        </v-card-text>
        <v-col cols="13" v-if="item.expanded">
            <div>
                <v-card-text class="text mt-2" v-for="(cur_item, key) in item.values" :key="key">
                    <v-row v-for="(value, key) in cur_item.values" :key="key" align="right" no-gutters>
                        <v-row align="left" no-gutters v-if="key === 0">
                            {{ cur_item.title }}
                        </v-row>
                        <v-col class="values" align="right">
                            {{ value }}
                        </v-col>
                    </v-row>
                </v-card-text>
            </div>
        </v-col>
    </v-card>
</template>

<style scoped>
.title {
    font-weight: 500;
    font-size: 1.3rem;
}

/* 
.text {
    font-size: 1rem;
} */
</style>


<script>

export default ({
    name: 'AppCardListSections',
    props: {
        item: {
            type: Object,
            required: true,
        },
    },
    setup() {
        return {}
    },
    data() {
        return {
            expandable: true,
            expanded: false,
        }
    },
    methods: {
        expand(item) {
            item.expanded = !item.expanded
        },
    },
})
</script>