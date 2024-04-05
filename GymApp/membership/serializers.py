from rest_framework import serializers

from GymApp.membership.models import MembershipPlan


class MembershipListSerializer(serializers.ModelSerializer):  # classes list

    gym = serializers.SlugRelatedField(
        many=False,  # it's by Default
        read_only=True,
        slug_field='name'
    )
    type_of = serializers.SlugRelatedField(
        many=False,  # it's by Default
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = MembershipPlan
        fields = ['plan', 'img', 'price', 'workouts',
                  'trainer']