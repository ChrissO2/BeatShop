<template>
    <tr>
        <td>{{ item.name }}</td>
        <td>${{ item.price }}</td>
        <td><button class="button is-danger is-rounded is-small" @click="removeFromCart(item)">Remove from cart</button></td>
    </tr>
</template>

<script>
export default {
    name: 'CartItem',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem
        }
    },
    methods: {
        removeFromCart() {
            this.$emit('removeFromCart', this.item)
        }
    },
}
</script>