<template>
    <div>
        <h1 align="center" @click="pula()">{{ payload.big_name }}</h1>
        <page-spoilers align="center" v-if="payload.spoilers" />
        <v-tabs v-model="tab" v-for="(value, key) in payload.items" :key="key" class="tab">
            <v-tab :value="value.name" @click="$emit('tab', value.name)">{{ value.name }}</v-tab>
        </v-tabs>
        <v-window v-model="tab" v-for="(value, key) in payload.items" :key="key">
            <v-window-item :value="value.name">
                <PageUnderConstruction v-if="value.under_construction" />
                <item-quote :quote="value.quote.quote" :author="value.quote.author" v-if="value.quote"/>
                <v-card-text v-if="value.about" class="text">
                    {{ value.about }}
                </v-card-text>
                <v-card-text v-if="value.chapter" class="text">
                    <v-card-text v-for="(chapter, key) in sortChapter(value.chapter)" :key="key">
                        <h2 @click="plm" @mouseover="chapter.hover = true" @mouseleave="chapter.hover = false"
                            :ref="chapter.number">
                            {{ chapter.name }}
                            <v-icon v-if="chapter.hover" @click="copy(chapter)"
                                title="Create a permalink to this chapter">
                                mdi-share
                            </v-icon>
                        </h2>
                        <ChapterDisclaimer v-if="chapter.disclaimer" :text="chapter.disclaimer" />
                        <v-card v-if="chapter.quote || chapter.image" flat>
                            <v-card-text class="quote-bg">
                                <v-row class="quote-bg">
                                    <v-col align="left" v-if="chapter.quote" class="quote-bg">
                                        <item-quote :quote="chapter.quote.quote" :author="chapter.quote.author" />
                                    </v-col>
                                    <v-col align="right" v-if="chapter.quote.image">
                                        <v-card-image :src="chapter.image" />
                                    </v-col>

                                </v-row>
                            </v-card-text>
                        </v-card>
                        <v-card-text v-if="chapter.text" class="text">
                            {{ chapter.text }}
                        </v-card-text>
                        <div v-if="chapter.sub_chapters" class="text">
                            <v-card-text v-for="(subchapter, key) in sortChapter(chapter.sub_chapters)" :key="key" class="quote-bg">
                                <h3 @mouseover="subchapter.hover = true" @mouseleave="subchapter.hover = false"
                                    :ref="subchapter.number">
                                    {{ subchapter.name }}
                                    <v-icon v-if="subchapter.hover" @click="copy(subchapter)"
                                        title="Create a permalink to this subchapter">
                                        mdi-share
                                    </v-icon>
                                </h3>
                                <ChapterDisclaimer v-if="subchapter.disclaimer" :text="subchapter.disclaimer" />
                                <v-card v-if="chapter.quote" class="quote-bg">
                                    <v-card-text class="quote-bg">
                                        <item-quote :quote="subchapter.quote.quote" :author="subchapter.quote.author"
                                            v-if="subchapter.quote" />
                                    </v-card-text>
                                </v-card>

                                <v-card-text v-if="subchapter.text" class="text">
                                    {{ subchapter.text }}
                                </v-card-text>
                            </v-card-text>
                        </div>
                    </v-card-text>
                </v-card-text>
            </v-window-item>
        </v-window>
    </div>
</template>

<style scoped>
.text {
    font-size: 1rem;
}
.tab {
    color: orange
}
.quote-bg{
    background-color: #414141;
    color:white;
}
</style>

<script>
import PageSpoilers from './PageSpoilers.vue'
import ItemQuote from './ItemQuote.vue'
import ChapterDisclaimer from './ChapterDisclaimer.vue'
import PageUnderConstruction from './PageUnderConstruction.vue'

export default {

    name: 'ItemView',
    setup() {
        return {}
    },
    components: {
    PageSpoilers,
    ItemQuote,
    ChapterDisclaimer,
    PageUnderConstruction,
},
    data() {
        return {
            hover: false,
            tab: null,
            refs_changed: false
        }
    },
    props: {
        payload: {
            type: Object,
            required: true,
        }
    },
    methods: {
        plm() {
            console.log(this.$refs)
        },
        copy(item) {
            console.log(item)
            const text_to_copy = `${window.location.host}${window.location.pathname}#${item.number}`
            navigator.clipboard.writeText(text_to_copy).finally(() => {
                console.log(`Copied ${text_to_copy} to clipboard`)
            })
        },
        scrollIntoView(item) {
            this.$refs[item][0].scrollIntoView({
                behavior: 'smooth',
            })
        },
        sortChapter(chapter){
            try {
                return chapter.sort((a, b) => (a.number > b.number) ? 1 : -1)
            }
            catch (e) {
                return chapter
            }
        },
    },
    created() {
    },
    computed: {
        slug() {
            return this.$route.params.slug
        },
        content() {
            return this.payload.data
        },
    },
    watch: {
        refs_changed: {
            handler: function () {
                this.$nextTick(() => {
                    if (this.$route.hash) {
                        this.scrollIntoView(this.$route.hash.slice(1))
                    }
                })

            },
            deep: true
        }
    },
    mounted(){
        this.refs_changed = true;
    },

    emits: ['tab'],

}
</script>
