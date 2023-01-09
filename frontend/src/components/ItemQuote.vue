<template>
    <div>
        <v-card flat>
            <v-row>
                <v-col align="left">
                    <v-row>
                        <v-col align="left">
                            <v-card-text>
                                <v-icon>mdi-format-quote-open</v-icon>
                                {{ removeFirstAndLastQuote(quote) }}
                                <v-icon>mdi-format-quote-close</v-icon>
                            </v-card-text>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col align="right">
                            <v-card-text>
                                - {{ author }}
                            </v-card-text>
                        </v-col>
                    </v-row>
                </v-col>
                <v-col align="right" v-if="image">
                    <v-image :src="image" />
                </v-col>
            </v-row>
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
        },
        image: {
            type: String,
            required: false,
        }
    },
    methods:{
        checkQuote(first_char){
            const quotes = [`“`, `”`, `"`, `'`]
            if (first_char == undefined){
                return false
            }
            for (var eachChar of quotes){
                if (eachChar == first_char){
                    return true
                }
            }
        },
        removeFirstAndLastQuote(quote){
            if (this.checkQuote(quote[0])) {
                quote = quote.slice(1)
            }
            if (this.checkQuote(quote[quote.length - 1])) {
                quote = quote.slice(0, -1)
            }
            return quote
        },
    },
}
</script>
