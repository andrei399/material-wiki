<template>
    <v-card elevation="4" shaped outlined>
        <v-card-text align="center" class="mx-0">
            <v-row>
                <!-- Center the element below -->
                <v-spacer class="mt-2 mb-3 bf">
                    <v-title>
                        TITLU
                    </v-title>
                </v-spacer>
            </v-row>
            <v-img height="200" src="https://cdn.vuetifyjs.com/images/cards/cooking.png"></v-img>
            <v-row class="mt-1">
                In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is available
            </v-row>
        </v-card-text>
    </v-card>
</template>

<style scoped>
   /* change font size for v-title */
    .bf {
         font-size: 1.5rem;
    }
</style>

<script>
import { defineComponent } from '@vue/composition-api'

export default defineComponent({
    setup() {
        return {}
    },
    data() {
        return {
            info: null,
        }
    },
    mounted() {
        this.$axios.get('localhost:8000/api/recipes').then((response) => {
            this.info = response.data
        })

    },
})
</script>
