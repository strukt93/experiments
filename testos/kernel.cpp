void printf(char* str){
    // The memory address where text starts (read by the bios)
    unsigned short* videoMemory = (unsigned short*) 0xb8000;
    for(int i = 0; str[i] != '\n';++i){
        // Keep the high bits and remove the lower ones.
        // Then do a logical OR with the value to get it
        // into the low bits.
        videoMemory[i] = (videoMemory[i] & 0xFF00) |  str[i];
    }
}

extern "C" void kernelMain(void* multiboot_structure, unsigned int magicnumber){
    printf("Hello world! --- https://twitter.com/strukt93");
    while(1);
}