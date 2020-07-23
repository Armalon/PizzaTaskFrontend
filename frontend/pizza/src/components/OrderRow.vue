<template>
    <tr>
        {{ element }}
        <th scope="row">{{ element.id }}</th>
        <td>{{ element.name }}</td>
        <td>
        </td>
        <td>
        </td>
        <td>
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

