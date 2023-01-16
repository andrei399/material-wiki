<template>
    <orange />
    <div class="disclaimer">
        <p>{{text}}</p>
    </div>
</template>

<script>
import orange from '@/assets/styles/orange.vue';

export default {
    name: 'ChapterDisclaimer',
    components: { orange },
    props: {
        text: {
            type: String,
            required: true,
        },
    },
}
</script>