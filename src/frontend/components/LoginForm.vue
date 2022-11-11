<template lang="">
    <FormKit
        type="form"
        submit-label="Login"
        incomplete-message="We are unable to process your login request at this time."
        :actions="false"
        :classes="{
            form: 'flex flex-col gap-y-4 bg-base-200 drop-shadow-sm p-4 rounded text-base-content w-full h-fit my-auto',
        }"
    >
        <FormKit
            type="email"
            label="Email"
            validation="required|email"
            validation-visibility="live"
            placeholder="admin@valink.io"
            :classes="{
                input: 'input input-bordered w-full',
                wrapper: 'mb-1.5',
                label: 'border-l-2 border-purple-500 pl-2 text-lg mb-2',
                error: 'text-red-500 text-xs',
                success: 'text-green-500 text-xs'
            }"
        />

        <FormKit
            type="password"
            name="password"
            value="super-secret"
            label="Password"
            validation="required"
            validation-visibility="live"
            :classes="{
                input: 'input input-bordered w-full',
                wrapper: 'mb-1.5',
                label: 'border-l-2 border-purple-500 pl-2 text-lg mb-2',
                error: 'text-red-500 text-xs',
                success: 'text-green-500 text-xs'
            }"
        />

        <FormKit
            type="submit"
            label="Login"
            :classes="{
                input: 'btn btn-primary btn-block',
                label: 'label',
                error: 'text-red-500 text-xs',
                success: 'text-green-500 text-xs'
            }"
        />
    </FormKit>
</template>
<script>
export default {
    
}
</script>
<style lang="">
    
</style>