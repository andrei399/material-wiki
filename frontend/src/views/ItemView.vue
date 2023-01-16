<template>
    <v-app :v-if="my_data" class="bg">
        <three-column class="bg">
            <v-main class="bg">
                <v-app-bar>
                
                    <v-tabs class="ui-elem" color="orange">
                        <v-tab>Dashboard</v-tab>
                        <v-tab>Messages</v-tab>
                        <v-tab>Profile</v-tab>
                        <v-tab>Updates</v-tab>
                    </v-tabs>
                </v-app-bar>
                <v-container>
                    <v-row>
                        <v-col cols="12" sm="2" class="mx-auto">
                            <v-sheet elevation="3" dark rounded="lg" min-height="268" class="ui-elem">
                                <PageTimeline :payload="my_data" :tab="this.tab" />
                            </v-sheet>
                        </v-col>
                        <v-col cols="12" sm="7" class="mx-auto">
                            <v-sheet elevation="3" min-height="70vh" rounded="lg" class="ui-elem">
                                <PageMain :payload="my_data" @tab="change_timeline" />
                            </v-sheet>
                        </v-col>
                        <v-col cols="12" sm="3" class="mx-auto">
                            <v-sheet rounded="lg" min-height="268" >
                                <AppCard :payload="my_data" :tab="this.tab" class="ui-elem"/>
                            </v-sheet>
                        </v-col>
                    </v-row>
                </v-container>
            </v-main>
        </three-column>
    </v-app>
    <UniversalFooter />
</template>

<style>
.bg {
    background-color: #212121;
    color: #212121;
}
.ui-elem{
    background-color: #414141;
    color: white;
}
.v-toolbar__content {
    background-color: #414141;
    color: white;
}
.vtab {
    color: orange;
}
</style>


<script>

import UniversalFooter from '@/components/UniversalFooter.vue';
import { md3 } from 'vuetify/blueprints';
import AppCard from '../components/AppCard.vue';
import PageMain from '../components/PageMain.vue';
import PageTimeline from '../components/PageTimeline.vue';

export default {
    name: 'TestWireframe',
    blueprints: md3,
    components: {
    AppCard,
    PageMain,
    PageTimeline,
    UniversalFooter
},
    computed: {
        slug() {
            return this.$route.params.slug
        }
    },
    async created() {
        console.log(this.theme)
        var cur_data = await this.$axios.get(`http://127.0.0.1:8000/api/page/${this.slug}`).catch(err => {
            console.log(err.request.status)
            this.$router.push({ path: '/404' })
        })
        this.my_data = cur_data.data
        this.tab = this.my_data.items[0].name
    },
    data() {
        return {
            my_data: Object,
            tab: String,
        }
    },
    methods: {
        change_timeline(tab) {
            this.tab = tab
        }
    },

};
</script>