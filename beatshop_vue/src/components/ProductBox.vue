<template>
    <div class="column is-3">
        <div class="box">
            <figure class="image mb-4">
                <img v-bind:src="product.get_image_resized">
            </figure>

            <h3 class="is-size-4">{{ product.name }}</h3>
            <p class="is-size-6 has-text-grey">${{ product.price }}</p>
            <audio :src="product.get_audio_file"
                type="audio/mp3"
                controlsList="nodownload"
                controls
                class="custom-audio">
            </audio>

            <div class="control">
                <a class="button is-dark" @click="addToCart(product)">Add to cart</a>
            </div>
        </div>
    </div>
</template>

<script>
import { mapMutations } from 'vuex'
import { toast } from 'bulma-toast'

export default {
    name: 'ProductBox',
    props: {
        product: Object
    },
    methods: {
        addToCart(product) {
            this.$store.commit('initializeStore')
            this.$store.commit('addToCart', product);

            toast({
                message: 'Product was added to the cart',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })

        },
    }
}
</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
    align-items: center;
  }

  .custom-audio {
    width: 100%;
    margin-top: 15px;
    margin-bottom: 15px;
    }
</style>