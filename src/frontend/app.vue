<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>
<style>
html {
  @apply m-0 p-0 bg-base-100;
}
body {
  font-family: 'PT Sans', sans-serif;
}
h1, h2, h3, h4, h5, h6 {
  font-family: 'Nunito', sans-serif;
}
.grad-text {
  @apply bg-clip-text text-transparent bg-gradient-to-br from-purple-400 to-pink-500 font-bold;
}
</style>