<template>
    <v-container>
        <v-card elevation="3" width="90%" align="center" class="mx-auto card-bg outline-title" rounded="xl" shaped
            outlined>
            <v-row class="tcs-title">
                <v-spacer />
                <v-card-title class="mt-5 mb-2" align="center">SOCIAL MEDIA</v-card-title>
                <v-spacer />
            </v-row>
            <v-row class="card-bg">
                <v-row class="ml-4 mr-4 mt-4 mb-6" align="center">
                    <v-btn v-for="item in item" :key="item.id" :href="item.link" target="_blank"
                        class="mx-auto rounded-xl">
                        <v-icon>{{ item.icon }}</v-icon>
                    </v-btn>
                </v-row>
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
    name: "SocialMediaHome",
    props: {
        item: {
            type: Array,
            required: true
        }
    },
    setup() {
        return {}
    },
}
</script>