<template>
    <v-card elevation="3" class="mb-2 mt-4" shaped outlined>
        <v-card-text class="title" align="center">
            <v-title @click="expand(item)" class="white-clr">
                {{ item.name }}
                <v-icon v-if="item.expandable && !item.expanded">mdi-chevron-down</v-icon>
                <v-icon v-else-if="item.expandable && item.expanded">mdi-chevron-up</v-icon>
            </v-title>
        </v-card-text>
        <v-card-text align="center" class="text" v-if="(item.expanded && item.expandable) || (!item.expandable)">
            {{ item.text }}
        </v-card-text>
    </v-card>
</template>

<style scoped>
.title {
    font-weight: 500;
    font-size: 1.3rem;
    background-color: rgb(194, 128, 4);
    /* background-color: #314B75 */
    /* Change text color to be pretty with background color */
}
.white-clr {
    color: white;
}
.text {
    font-size: 1rem;
}
</style>

<script>
export default ({
    name: "AppCardTextSections",
    props: {
        item: {
            type: Object,
            required: true,
        }
    },
    data(){
        return {
            expanded: false,
        }
    },
    created(){
        // console.log(this.item)
    },
    methods: {
        expand(item){
            if(item.expandable){
                item.expanded = !item.expanded
            }
        },
        test(item){
            item.expandable = !item.expandable
            console.log(item)
        }
    },
    setup() {
        return {};
    },
})
</script>
