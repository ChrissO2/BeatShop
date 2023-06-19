<template>
    <div class="box mb-4">
        <h3 class="is-size-4 mb-6">Order #{{ order.id }}</h3>

        <h4 class="is-size-5">Products</h4>

        <table class="table is-fullwidth">
            <thead>
                <tr>
                    <th>Product</th>
                    <th>Price</th>
                    <th>Downloads</th>
                </tr>
            </thead>

            <tbody>
                <tr
                    v-for="item in order.items"
                    v-bind:key="item.product.id"
                >
                    <td>{{ item.product.name }}</td>
                    <td>${{ item.product.price }}</td>
                    <td>
                        <button class="button is-success is-rounded" @click="redirectToDownload(item.product.id)">Download</button>
                    </td>
                </tr>
                <tr>Total price: {{ orderTotalPrice }}</tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import axios, { Axios } from 'axios'

export default {
    name: 'OrderSummary',
    props: {
        order: Object
    },
    methods: {
        redirectToDownload(productId) {
            const downloadLink = 'http://localhost:8000/api/products/' + productId + '/'
            window.location.href = downloadLink;
        }
    },
    computed: {
        orderTotalPrice() {
            let totalPrice = 0
            for (let i = 0; i < this.order.items.length; i++) {
                totalPrice += parseFloat(this.order.items[i].price)
            }
            return totalPrice.toFixed(2)
        },
    }
}
</script>