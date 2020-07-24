<template>
    <tr>
        <th scope="row">{{ element.id }}</th>
        <td>{{ element.user_name }}</td>
        <td>
            {{ element.address }}
        </td>
        <td>
            {{ element.phone }}
        </td>
        <td>
             {{ element.create_timestamp | formatTimestampDateTime }}
        </td>
        <td class="text-nowrap">
            {{ element.status | capitalize }}
            <span class="text-success" v-if="element.status_countdown">({{ Math.round(element.status_countdown) }})</span>
        </td>
        <td>
            {{ formatPriceByCurrency(element.total_price) }}
        </td>
    </tr>
</template>

<script>
    export default {
        props: ['element'],
        computed: {
        }
    }
</script>

