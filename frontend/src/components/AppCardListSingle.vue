<template>
    <v-card>
        <v-row>
            <v-col v-for="(item, key) in values" :key="key">
                <AppCardListSingle :values="item.values"/>
            </v-col>
        </v-row>
    </v-card>
</template>

<script>
export default {
    name: 'AppCardListSingle',
    props: {
        values: {
            type: Array,
            required: true,
        },
    },
    setup() {
        return {}
    },
}
</script>