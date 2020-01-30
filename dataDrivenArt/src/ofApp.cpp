#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
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
	while (receiver.hasWaitingMessages()) {
		ofxOscMessage m;

		receiver.getNextMessage(m);

		//oscMessage = m.getArgAsInt32(0);
		oscMessage = m.getArgAsFloat(0);
		console("address") << oscMessage << " " << m.getNumArgs();

		cameraImage.load("export/export.png");

		/*
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
		*/
		
		if (m.getAddress() == "/vol") {
			vol = oscMessage;
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
	shader.setUniform1f("vol", vol);
	shader.setUniform1f("time", ofGetElapsedTimef());

	ofDrawRectangle(0, 0, ofGetWidth(), ofGetHeight());
	shader.end();

	console.print(40, 40);
}
