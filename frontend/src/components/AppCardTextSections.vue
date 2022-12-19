<template>
    <v-card elevation="3" class="ml-3 mt-5 mb-10" shaped outlined>
        <v-card-text align="center">
            <v-title class="title">
                {{ item.title }}
            </v-title>
        </v-card-text>
        <v-card-text align="center" class="text">
            {{ item.value }}
        </v-card-text>
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
export default ({
    name: "AppCardTextSections",
    props: {
        item: {
            type: Object,
            required: true,
        }
    },
    setup() {
        return {};
    },
})
</script>
