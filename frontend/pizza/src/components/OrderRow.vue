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
        <td>
            {{ element.status }}
        </td>
        <td>
            ${{ element.total_price }}
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

