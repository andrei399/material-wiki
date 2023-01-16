<template>
    <v-container>
        <v-card elevation="3" width="90%" align="center" class="mx-auto card-bg outline-title" rounded="xl" shaped
            outlined>
            <v-row class="tcs-title">
                <v-spacer />
                <v-card-title class="mt-5 mb-2" align="center"> {{ item.title }}</v-card-title>
                <v-spacer />
            </v-row>
            <v-row class="card-bg" aria-colcount="12">
                <v-col sm="1" class="mr-2 mb-2 ml-2 " v-if="item.image != null">
                    <v-img :src="item.image.image" :title="item.image.name" height="130" align="left" />
                </v-col>
                <v-col align="left">
                    <v-card-text>{{ item.text }}</v-card-text>
                </v-col>
            </v-row>
        </v-card>
    </v-container>
</template>

<style scoped>
.outline-title {
    border: 4px solid rgb(194, 128, 4);
}
</style>

<script>

export default {
    name: "HomeItemCard",
    props: {
        item: {
            type: Object,
            required: true
        }
    },
}

</script>