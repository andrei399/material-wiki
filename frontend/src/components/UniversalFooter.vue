<template>
    <v-footer class="footer-bg text-center d-flex flex-column" v-if="my_data != null">
        <div>
            <v-btn v-for="icon in my_data.socials" :key="icon" class="mx-4" :icon="icon.icon" :href="icon.link"
                target="_blank" color="white" :variant="remove_mdi_prefix(icon.icon)"></v-btn>
        </div>
        <v-divider />
        <v-row aria-colcount="12" align="left" dense>
            <v-col align="left" justify="center" fill-height>
                <v-img :src="my_data.image.image" :alt="my_data.image.name" :title="my_data.image.name" height="100"
                    width="200"></v-img>
            </v-col>
            <v-col v-for="section in my_data.sections" :key="section.id" align="right">
                <v-card-title class="" align="center">{{ section.title }}</v-card-title>
                    <v-row align="center" no-gutters v-for="item in section.links" :key="item.id">
                        <v-col align="center"><a :href="item.link" class="plm"><p color="white">{{ item.text }}</p></a></v-col>
                    </v-row>
            </v-col>
        </v-row>

        <v-divider />

        <div>
            {{ new Date().getFullYear() }} — <strong>Andrei399</strong>
        </div>
    </v-footer>
</template>

<style>
.plm {
    color: yellow;
    text-decoration: none;
}
.footer-bg{
    background-color: #280033;
    /* color: #280033; */
}
</style>

<script>
export default {
    name: 'UniversalFooter',
    data: () => ({
        my_data: null,
    }),
    methods: {
        remove_mdi_prefix(icon) {
            return icon.replace('mdi-', '')
        },
    },
    async created() {
        var req = await this.$axios.get('http://127.0.0.1:8000/api/home/footer')
        this.my_data = req.data[0]
    },
}
</script>