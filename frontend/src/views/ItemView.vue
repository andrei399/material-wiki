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
                        <v-col cols="12" sm="2" class="mx-auto">
                            <v-sheet elevation="3" dark rounded="lg" min-height="268">
                                <h1 class="pa-3 ml-3" center>List of contents</h1>
                                <v-list-item>
                                    <v-list-item-content>
                                        <v-list-item-title>Single-line item</v-list-item-title>
                                    </v-list-item-content>
                                </v-list-item>

                                <v-list-item two-line>
                                    <v-list-item-content>
                                        <v-list-item-title>Two-line item</v-list-item-title>
                                        <v-list-item-subtitle>Secondary text</v-list-item-subtitle>
                                    </v-list-item-content>
                                </v-list-item>

                                <v-list-item three-line>
                                    <v-list-item-content>
                                        <v-list-item-title>Three-line item</v-list-item-title>
                                        <v-list-item-subtitle>
                                            Secondary line text Lorem ipsum dolor sit amet,
                                        </v-list-item-subtitle>
                                        <v-list-item-subtitle>
                                            consectetur adipiscing elit.
                                        </v-list-item-subtitle>
                                    </v-list-item-content>
                                </v-list-item>
                            </v-sheet>
                        </v-col>
                        <v-col cols="12" sm="7" class="mx-auto">
                            <v-sheet elevation="3" min-height="70vh" rounded="lg">
                                <h1>Detailed info about the topic</h1>
                            </v-sheet>
                        </v-col>
                        <v-col cols="12" sm="3" class="mx-auto">
                            <v-sheet rounded="lg" min-height="268">
                                <AppCard />
                            </v-sheet>
                        </v-col>
                    </v-row>
                </v-container>
            </v-main>
        </three-column>
    </v-app>
</template>

<script>
import AppCard from '../components/AppCard.vue';

export default {
    name: 'TestWireframe',
    components: {
        AppCard,
    },
};
</script>