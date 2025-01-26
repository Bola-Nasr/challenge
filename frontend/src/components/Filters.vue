<template>
  <div class="bg-white p-4 rounded-lg shadow-md mb-4">
    <h2 class="text-xl font-semibold mb-4">Filters</h2>
    <div class="space-y-4">
      <input v-model="fullAddress" type="text" placeholder="Full Address" class="w-full p-3 border rounded-lg" />
      <input v-model="classDescription" type="text" placeholder="Class Description" class="w-full p-3 border rounded-lg" />
      <input v-model="minMarketValue" type="number" placeholder="Min Market Value" class="w-full p-3 border rounded-lg" />
      <input v-model="maxMarketValue" type="number" placeholder="Max Market Value" class="w-full p-3 border rounded-lg" />
      <input v-model="buildingUse" type="text" placeholder="Building Use" class="w-full p-3 border rounded-lg" />
      <input v-model="minSquareFeet" type="number" placeholder="Min Square Feet" class="w-full p-3 border rounded-lg" />
      <input v-model="maxSquareFeet" type="number" placeholder="Max Square Feet" class="w-full p-3 border rounded-lg" />
      <select v-model="sortBy" class="w-full p-3 border rounded-lg">
        <option value="market_value_asc">Market Value Ascending</option>
        <option value="market_value_desc">Market Value Descending</option>
        <option value="square_feet_asc">Square Feet Ascending</option>
        <option value="square_feet_desc">Square Feet Descending</option>
      </select>
      <button @click="applyFilters" class="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700">Apply</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      fullAddress: '',
      classDescription: '',
      minMarketValue: null,
      maxMarketValue: null,
      buildingUse: '',
      minSquareFeet: null,
      maxSquareFeet: null,
      sortBy: 'market_value_asc',
    };
  },
  methods: {
    applyFilters() {
      this.$emit('apply-filters', {
        fullAddress: this.fullAddress,
        classDescription: this.classDescription,
        minMarketValue: this.minMarketValue,
        maxMarketValue: this.maxMarketValue,
        buildingUse: this.buildingUse,
        minSquareFeet: this.minSquareFeet,
        maxSquareFeet: this.maxSquareFeet,
        sortBy: this.sortBy,
      });
    },
  },
};
</script>