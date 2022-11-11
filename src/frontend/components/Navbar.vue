<template lang="">
    <div class="navbar bg-base-100 font-title">
        <div class="navbar-start">
            <button class="btn btn-ghost">
                <div class="flex flex-row gap-x-2 items-center">
                    <Icon name="charm:plus" size="20px"/>
                    <span class="hidden md:inline-block">New Link</span>
                </div>
            </button>
        </div>
        <div class="navbar-center">
            <NuxtLink to="/">
                <Logo class="h-12 hidden md:block"/>
                <LogoCompact class="h-12 block md:hidden"/>
            </NuxtLink>
        </div>
        <div class="navbar-end">
            <div class="dropdown dropdown-end">
                <label tabindex="0" class="btn btn-ghost">
                    <Icon name="charm:menu-hamburger"/>
                </label>
                <ul tabindex="0" class="menu menu-compact dropdown-content mt-3 p-2 shadow bg-base-100 rounded-box w-52">
                    <li v-for="(link, index) in links" :key="index">
                        <NuxtLink :to="link.path" class="menu-item">
                            <!-- <Icon :name="link.icon" class="mr-2"/> -->
                            <span>{{ link.name }}</span>
                        </NuxtLink>
                    </li>
                    <div class="divider"></div> 
                    <li><a class="text-red-500">Logout</a></li>
                </ul>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            links: [
                {
                    name: "Home",
                    path: "/"
                },
                {
                    name: "Dashbaord",
                    path: "/dashboard"
                },
                {
                    name: "Settings",
                    path: "/settings"
                },
            ]
        }
    }
}
</script>
<style lang="">
    
</style>