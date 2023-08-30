public class HelloJNI {
    static{
        System.loadLibrary("hello");
    }

    private native void sayHello();

    // Test Driver
    public static void main(String[] args){
        new HelloJNI().sayHello();
    }
}