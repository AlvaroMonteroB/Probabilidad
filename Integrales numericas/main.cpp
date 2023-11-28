#include<vector>
#include<iostream>
#include<cmath>
#include<fstream>

#define e 2.718281828
#define pi 3.141592654
using namespace std;

typedef struct{
    float b;
    float sum;
}Result;


float func1(float sigma, float miu,float x){
    return (pow(e,.5f*pow((x-miu)/sigma,2))
           /(sigma*pow(2*pi,.5f)));
}

float func2(float z){
    return pow(e,(-.5f)*pow(z,2))/sqrt(2*pi);
}

float integral1(float a,float b, float sigma, float miu, float dx){
    float sum=0,x=a;
    while(x<=b){
        sum+=func1(sigma,miu,x)*dx;
        x+=dx;
    }
    return sum;
}

void write_vector(vector<Result> resultado){
    ofstream f("Archivo.txt");
    if (!f.is_open()){
        cout<<"Archivo no encontrado\n";
        exit(2);
    }
    for(auto& pair:resultado){
        f<<"b= "<<pair.b<<" Res = "<<pair.sum<<" ,";
    }
    f.close();
    cout<<resultado.size()<<" resultados escritos";
}


void integral2(){
    float a=-6.0f,b0=-5.99f,delta=.01f,dz=0.0001f;
    vector<Result> entradas;
    while(b0<=6.0f){
        float z=a;
        float sum=0;
        while(z<=b0){
            sum+=func2(z)*dz;
            z+=dz;
        }
        Result integral={b0,sum};
        entradas.push_back(integral);
        b0+=delta;
    }
    write_vector(entradas);

} 


int main(){
char c;
float a,b,sigma=0,miu,dx=0.0001f;
cout<<"Introduce que funcion quieres ejecutar\n";
cin>>c;
switch (c)
{
case '1':
    cout<<"Introduce a\n";
    cin>>a;
    cout<<"Introduce b\n";
    cin>>b;
    while(sigma<=0){
        cout<<"Introduce sigma\n";
        cin>>sigma;
    }
    cout<<"Introduce miu\n";
    cin>>miu;
    float result;
    result= integral1(a,b,sigma,miu,dx);
    cout<<"El area bajo la curva de tu funcion es: "<<result<<'\n';

    break;
case '2':
    integral2();
    break;
default:
    break;
}

    return 0;
}