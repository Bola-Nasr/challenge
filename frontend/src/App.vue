<template>
  <div id="app" class="container mx-auto">
    <Login v-if="!loggedIn" @login-success="handleLoginSuccess" />
    <div v-else>
      <h2 class="text-xl font-semibold mb-4 text-center">W&D Property Management</h2>
      <div class="space-y-4">
        <Map :properties="properties" />
        <Filters @apply-filters="handleFilters" />
        <PropertyList :properties="properties" />
        <Pagination :currentPage="currentPage" :totalPages="totalPages" @change-page="changePage" />
      </div>
    </div>
  </div>
</template>

<script>
import Login from './components/Login.vue';
import Filters from './components/Filters.vue';
import Map from './components/Map.vue';
import PropertyList from './components/PropertyList.vue';
import Pagination from './components/Pagination.vue';
import { fetchProperties } from './services/api';

export default {
  components: { Login, Filters, Map, PropertyList, Pagination },
  data() {
    return {
      loggedIn: false,
      token: '',
      properties: [],
      currentPage: 1,
      totalPages: 1,
      filters: {
        fullAddress: '',
        classDescription: '',
        minMarketValue: null,
        maxMarketValue: null,
        buildingUse: '',
        minSquareFeet: null,
        maxSquareFeet: null,
        sortBy: 'market_value',
      },
    };
  },
  methods: {
    async handleLoginSuccess(token) {
      this.loggedIn = true;
      this.token = token;
      await this.fetchProperties();
    },
    async fetchProperties() {
      const data = await fetchProperties(this.token, this.currentPage, this.filters);
      this.properties = data.properties;
      this.totalPages = Math.ceil(data.total / 20);
    },
    changePage(page) {
      this.currentPage = page;
      this.fetchProperties();
    },
    handleFilters(filters) {
      this.filters = filters;
      this.fetchProperties();
    },
  },
};
</script>