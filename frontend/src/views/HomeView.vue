<template>
  <v-app id="material-wiki">
    <orange />
    <v-app-bar class="card-bg">
      <v-tabs class="ui-elem vtab" color="orange">
        <v-tab>Dashboard</v-tab>
        <v-tab>Messages</v-tab>
        <v-tab>Profile</v-tab>
        <v-tab>Updates</v-tab>
      </v-tabs>
    </v-app-bar>

    <v-main class="web-bg" >
      <template v-if="my_data">
        <v-container>
          <v-row>
            <v-col sm="10">
              <HomeItemCard v-for="(section, key) in my_data.sections" :key="key" :item="section" />
              <v-row>
                <PopularPage v-for="page in main_pages" :key="page.id" :items="page"/>
              </v-row>
            </v-col>
            <v-col>
              <HomeItemCard v-for="(section, key) in my_data.left_sections" :key="key" :item="section" />
              <SocialMediaHome :item="my_data.social_media"/>
              <RelatedWikiHome :items="my_data.related_wikis"/>
            </v-col>
          </v-row>
        </v-container>
      </template>
    </v-main>
  </v-app>
  <UniversalFooter />
</template>

<script>
// TODO: Refactor this file to use the new data structure

import { md3 } from 'vuetify/blueprints';
import orange from '@/assets/styles/orange.vue';
import HomeItemCard from '@/components/HomeItemCard.vue';
import SocialMediaHome from '@/components/SocialMediaHome.vue';
import RelatedWikiHome from '@/components/RelatedWikiHome.vue';
import UniversalFooter from '@/components/UniversalFooter.vue';
import PopularPage from '@/components/PopularPage.vue';

export default {
  name: 'HomeView',
  blueprint: md3,
  components: {
    orange,
    HomeItemCard,
    SocialMediaHome,
    RelatedWikiHome,
    UniversalFooter,
    PopularPage
},
  data: () => ({
    my_data: null,
    main_sections: null,
    main_pages: null,
    side_sections: null,
    side_pages: null,
  }),
  async created() {
    var req = await this.$axios.get('http://127.0.0.1:8000/api/home/')
      .catch()
      .then((response) => response.data);
    this.my_data = req[0]
    this.main_sections = this.my_data.sections.filter(section => section.type === 't')
    this.main_pages = this.my_data.sections.filter(section => section.type === 'p')
    this.side_sections = this.my_data.sections.filter(section => section.type === 'st')
    this.side_pages = this.my_data.sections.filter(section => section.type === 'sp')
    console.log(
      this.main_sections,
      this.main_pages,
      this.side_sections,
      this.side_pages,
    )
  }
}
</script>

<style>
.v-toolbar__content {
  background-color: #414141;
  color: white;
}
</style>