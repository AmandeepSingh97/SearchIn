from rest_framework.generics import RetrieveAPIView
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from SearchIn.user.serializers import UserRegistrationSerializer
from SearchIn.user.serializers import UserLoginSerializer


class UserRegistrationView(CreateAPIView):

    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)


    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
                'success': 'True',
                'status code': status_code,
                'message': 'User registered  successfully',
            }


        except Exception as e:
            status_code = status.HTTP_409_CONFLICT
            response = {
                'success': 'False',
                'status_code': status.HTTP_409_CONFLICT,
                'message': 'User already exists'
                'error': str(e)
            }

        return Response(response, status=status_code)


class UserLoginView(RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer


    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'True',
                'status code': status.HTTP_200_OK,
                'message': 'User logged in  successfully',
                'token': serializer.data['token'],
            }
        

        except Exception as e:
            status_code = status.HTTP_404_NOT_FOUND
           response={
               'success':'False',
               'status_code': status.HTTP_404_NOT_FOUND,
               'message': 'User does not exists'
               'error': str(e)
           }

        return Response(response, status=status_code)
