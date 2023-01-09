<template>
    <v-card align="center" cols="3" width="1000" height="80" class="mx-auto mt-5 mb-5" color="#E6E6E6">
        <v-row align="center" class="mt-3">
            <v-img src="http://localhost:8000/media/Tw3_achievements_bookworm_unlocked.webp" height="50" width="50" /> 
            <v-card-text>
                <v-row align="center">
                    <v-spacer />
                    <h4>"Do you really wish to know?"</h4>
                    <p>— Spoilers from the books and/or adaptations to follow!	</p>
                    <v-spacer />
                </v-row>
            </v-card-text>
            <v-img src="http://localhost:8000/media/Tw3_achievements_bookworm_unlocked.webp" height="50" width="50" /> 
        </v-row>
    </v-card>
</template>

<script>
export default {
    name: 'PageSpoilers',
    setup() {
        return {}
    },
}
</script>