#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
	soundStream.printDeviceList();

	int bufferSize = 256;

	left.assign(bufferSize, 0.0);
	right.assign(bufferSize, 0.0);
	volHistory.assign(400, 0.0);

	bufferCounter = 0;
	drawCounter = 0;
	smoothedVol = 0.0;
	scaledVol = 0.0;

	ofSoundStreamSettings settings;

	auto devices = soundStream.getMatchingDevices("defalt");
	if (!devices.empty()) {
		settings.setInDevice(devices[2]);
	}

	settings.setInListener(this);
	settings.sampleRate = 44100;
	settings.numOutputChannels = 0;
	settings.numInputChannels = 2;
	settings.bufferSize = bufferSize;
	soundStream.setup(settings);

	ofEnableDepthTest();

	shader.load("shader/shader.vert", "shader/shader.frag");

	fbo.allocate(ofGetWidth(), ofGetHeight());

	receiver.setup(PORT);

	ofDirectory dir(ofToDataPath("./images/"));

	total = dir.listDir();
	
	images.resize(total);

	for (int i = 0; i < total; i++) {
		loader.loadFromDisk(images[i], dir.getName(i));
		images[i].resize(640, 480);
	}
	cout << total << " images loaded" << endl;
}

//--------------------------------------------------------------
void ofApp::update(){
	//lets scale the vol up to a 0-1 range 
	scaledVol = ofMap(smoothedVol, 0.0, 0.17, 0.0, 1.0, true);

	//lets record the volume into an array
	volHistory.push_back(scaledVol);

	//if we are bigger the the size we want to record - lets drop the oldest value
	if (volHistory.size() >= 400) {
		volHistory.erase(volHistory.begin(), volHistory.begin() + 1);
	}

	while (receiver.hasWaitingMessages()) {
		ofxOscMessage m;

		receiver.getNextMessage(m);

		oscMessage = m.getArgAsInt32(0);
		console("address") << oscMessage << " " << m.getNumArgs();

		cameraImage.load("export/export.png");

		if (m.getAddress() == "/first") {
			std::string front = "images/";
			std::string back = ".jpg";
			std::string path = front + std::to_string(oscMessage) + back;
			console(path);
			firstImage.load(path);
			osc1 = oscMessage;
		}

		if (m.getAddress() == "/second") {
			std::string front = "images/";
			std::string back = ".jpg";
			std::string path = front + std::to_string(oscMessage) + back;
			console(path);
			secondImage.load(path);
			osc2 = oscMessage;
		}

		if (m.getAddress() == "/third") {
			std::string front = "images/";
			std::string back = ".jpg";
			std::string path = front + std::to_string(oscMessage) + back;
			console(path);
			thirdImage.load(path);
			osc3 = oscMessage;
		}
	}
}

//--------------------------------------------------------------
void ofApp::draw(){
	fbo.begin();
	ofClear(0, 0, 0, 0);
	ofPushMatrix();
	ofTranslate(ofGetWidth() / 2, ofGetHeight() / 2);

	cam.begin();

	cam.end();

	ofPopMatrix();

	cameraImage.draw(0, ofGetHeight() / 2, ofGetWidth() / 2, ofGetHeight() / 2);
	firstImage.draw(0, 0, ofGetWidth() / 2, ofGetHeight() / 2);
	secondImage.draw(ofGetWidth() / 2, 0, ofGetWidth() / 2, ofGetHeight() / 2);
	thirdImage.draw(ofGetWidth() / 2, ofGetHeight() / 2, ofGetWidth() / 2, ofGetHeight() / 2);

	fbo.end();

	// PostEffect
	shader.begin();
	shader.setUniformTexture("texture", fbo, 0);
	shader.setUniform2f("resolution", ofGetWidth(), ofGetHeight());
	shader.setUniform1f("vol", smoothedVol);
	shader.setUniform1f("number1", osc1);
	shader.setUniform1f("number2", osc2);
	shader.setUniform1f("number3", osc3);
	shader.setUniform1f("time", ofGetElapsedTimef());

	ofDrawRectangle(0, 0, ofGetWidth(), ofGetHeight());
	shader.end();

	console.print(40, 40);
}

//--------------------------------------------------------------
void ofApp::audioIn(ofSoundBuffer & input) {

	float curVol = 0.0;

	// samples are "interleaved"
	int numCounted = 0;

	//lets go through each sample and calculate the root mean square which is a rough way to calculate volume	
	for (size_t i = 0; i < input.getNumFrames(); i++) {
		left[i] = input[i * 2] * 0.5;
		right[i] = input[i * 2 + 1] * 0.5;

		curVol += left[i] * left[i];
		curVol += right[i] * right[i];
		numCounted += 2;
	}

	//this is how we get the mean of rms :) 
	curVol /= (float)numCounted;

	// this is how we get the root of rms :) 
	curVol = sqrt(curVol);

	smoothedVol *= 0.93;
	smoothedVol += 0.07 * curVol;

	bufferCounter++;

}