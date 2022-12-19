<template>
  <v-app>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  theme: {
    dark: true,
  },
  data: () => ({
    //
  }),
}
</script>
