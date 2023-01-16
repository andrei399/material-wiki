<template>
    <v-container>
        <v-card elevation="3" width="90%" align="center" class="mx-auto card-bg outline-title" rounded="xl" shaped
            outlined>
            <v-row class="tcs-title">
                <v-spacer />
                <v-card-title class="mt-5 mb-2" align="center">RELATED WIKIS</v-card-title>
                <v-spacer />
            </v-row>
            <v-row class="card-bg" v-for="item in items" :key="item.id">
                <v-row class="ml-4 mr-4 mt-4 mb-6" align="center">
                        <v-img v-if="item.image != null" :src="item.image.image" :href="item.image.links_to" :alt="item.image.name"
                            :title="item.image.name" height="100" width="80%" @click="redirect_to_wiki(item.link)" class="clickable">
                        </v-img>
                    <v-card-text v-else>{{ item.name }}</v-card-text>
                </v-row>
            </v-row>
        </v-card>
    </v-container>
</template>

<style scoped>
.outline-title {
    border: 4px solid rgb(194, 128, 4);
}
.clickable {
    cursor: pointer;
}
</style>

<script>
export default {
    name: 'RelatedWikiHome',
    props: {
        items: {
            type: Array,
            required: true,
        }
    },
    methods: {
        redirect_to_wiki(link) {
            window.location.replace(link)
        },
    },
}
</script>