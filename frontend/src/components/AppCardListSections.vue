<template>
    <v-card elevation="3" class="mb-2 mt-2" shaped outlined>
        <v-card-text align="center" @click="expand(item)" class="title" :class="{'expandable': item.expandable}">
            <v-card-title class="title white-clr">
                <v-row align="center">
                    <v-spacer />
                    {{ item.name }}
                    <div v-if="item.expandable">
                        <v-icon v-if="item.expanded">mdi-chevron-down</v-icon>
                        <v-icon v-else>mdi-chevron-up</v-icon>
                    </div>
                    <v-spacer />
                </v-row>
            </v-card-title>
        </v-card-text>
        <v-col cols="13" v-if="(item.expanded && item.expandable) || (!item.expandable)">
            <div>
                <v-card-text class="text mt-2" v-for="(cur_item, key) in item.list" :key="key" >
                    <v-row no-gutters align="right">
                        <v-row>
                            {{ cur_item.left }}
                        </v-row>
                        <v-col align="right" >
                            <v-row v-for="(value, key) in cur_item.right" :key="key" no-gutter class="right" align="right">
                                    {{ value.value }}
                            </v-row>
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
    background-color: rgb(194, 128, 4);
    /* background-color: #314B75; */
}

.white-clr {
    color: white;
}

.leftbg {
    background-color: #282828;
    color: white;
}

.expandable:hover {
    cursor: pointer;
}
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
            expanded: false,
            hovering: false,
        }
    },
    methods: {
        expand(item) {
            if (item.expandable) {
                item.expanded = !item.expanded

            }
        },
    },
})
</script>