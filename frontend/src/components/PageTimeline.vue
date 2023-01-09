<template>
    <h1 @click="test()" align="center">Contents</h1>
    <v-timeline align-top align="center" side="start" truncate-line="both">
        <template v-for="(chapter, key) in sortChapter(timeline.chapter)" :key="key">
            <v-timeline-item dot-color="purple" @click="scrollIntoView(chapter.number)">
                <template v-slot:opposite>
                    {{ chapter.name }}
                </template>
                {{ chapter.number }}
            </v-timeline-item>
            <v-timeline-item v-for="(subchapter, key) in sortChapter(chapter.sub_chapters)" :key="key" @click="scrollIntoView(subchapter.number)">
                <template v-slot:opposite>
                    {{ subchapter.name }}
                </template>
                {{ subchapter.number }}
            </v-timeline-item>
        </template>
    </v-timeline>
</template>

<style scoped>
.right {
    text-align: right;
}
</style>

<script>
import router from '@/router'

export default {
    name: 'PageTimeline',
    setup() {
        return {}
    },
    props: {
        payload: {
            type: Object,
            required: true,
        },
        tab: {
            type: String,
            required: true,
        }
    },
    async created() {
        this.timeline = this.payload.items.filter(item => item.name == this.tab)[0]
        // console.log('plm')
    },
    methods: {
        test() {
            // console.log
        },
        sortChapter(chapter) {
            //Sort chapter array based on chapter.number
            try {
                return chapter.sort((a, b) => (a.number > b.number) ? 1 : -1)
            }
            catch (e) {
                return chapter
            }
        },
        scrollIntoView(item) {
            console.log(`${window.location.pathname}#${item}`)
            router.replace({ path: `${window.location.pathname}#${item}` })
        },
    },
}

</script>