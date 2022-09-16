<script setup lang="ts">
    import { ref } from 'vue'
    
    const props = defineProps({
      count: {
        default: 0,
      },
    })
    
    const counter = ref(props.count)
</script>

<template>
    <div flex="~" w="min" border="~ gray-400 opacity-50 rounded-md">
        <span>$ {{count}}</span>
    </div>
</template>
    