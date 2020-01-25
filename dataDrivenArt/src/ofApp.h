#pragma once

#include "ofMain.h"
#include "ofxOsc.h"
#include "ScreenConsole.h"
#include "ofxThreadedImageLoader.h"

#define HOST "127.0.0.1"
#define PORT 54415

class ofApp : public ofBaseApp {

public:
	void setup();
	void update();
	void draw();
	ofxOscReceiver receiver;
	int oscMessage;
	float osc1;
	float osc2;
	float osc3;
	ScreenConsole console;
	ofImage cameraImage;
	ofImage firstImage;
	ofImage secondImage;
	ofImage thirdImage;
	ofxThreadedImageLoader loader;
	vector<ofImage> images;
	int total;

	void audioIn(float * input, int bufferSize, int nChannels);
	ofSoundStream soundStream;
	float curVol;
	
	ofShader shader;
	ofFbo fbo;
	ofEasyCam cam;
};