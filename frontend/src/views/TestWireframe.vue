<template>
    <v-app>
        <three-column>
            <v-main>
                <v-app-bar>
                    <v-tabs>
                        <v-tab>Dashboard</v-tab>
                        <v-tab>Messages</v-tab>
                        <v-tab>Profile</v-tab>
                        <v-tab>Updates</v-tab>
                    </v-tabs>
                </v-app-bar>
                <v-container>
                    <v-row>
                        <v-col cols="12" sm="2">
                            <v-sheet rounded="lg" min-height="268">
                                <!--  -->
                            </v-sheet>
                        </v-col>
                        <v-col cols="12" sm="7">
                            <v-sheet min-height="70vh" rounded="lg">
                                <h1>See Width</h1>
                            </v-sheet>
                        </v-col>
                        <v-col cols="12" sm="3">
                            <v-sheet rounded="lg" min-height="268">
                                <TestLayout />
                            </v-sheet>
                        </v-col>
                    </v-row>
                </v-container>
            </v-main>
        </three-column>
    </v-app>
</template>

<script>
import TestLayout from '../components/TestLayout.vue';

export default {
    name: 'TestWireframe',
    components: {
        TestLayout,
    },
};
</script>