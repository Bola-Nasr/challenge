<template>
  <div class="space-y-4 mt-4">
    <div v-for="property in properties" :key="property.id" class="bg-white p-4 rounded-lg shadow-md">
      <h3 class="text-lg font-bold">Property ID: {{ property.id }}</h3>
      <p><strong>Address:</strong> {{ property.full_address }}</p>
      <p><strong>Class:</strong> {{ property.class_description }}</p>
      <p><strong>Value:</strong> {{ property.estimated_market_value }}</p>
      <p><strong>Use:</strong> {{ property.building_use }}</p>
      <p><strong>Size:</strong> {{ property.building_square_feet }} sq. ft.</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    properties: {
      type: Array,
      required: true,
    },
  },
};
</script>
