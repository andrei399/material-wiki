<template>
    <div>
        <v-card flat>
            <v-card-text>
                {{ quote }}
            </v-card-text>
            <v-card-text>
                {{ author }}
            </v-card-text>
        </v-card>
    </div>
</template>

<script>
export default {
    name: 'ItemQuote',
    setup() {
        return {}
    },
    props: {
        quote: {
            type: String,
            required: true,
        },
        author: {
            type: String,
            required: true,
        }
    },
}
</script>
