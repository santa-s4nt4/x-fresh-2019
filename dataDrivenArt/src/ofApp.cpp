#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
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

		oscMessage = m.getArgAsInt32(0);
		console("address") << oscMessage << " " << m.getNumArgs();

		if (m.getAddress() == "/image") {
			std::string front = "images/";
			std::string back = ".jpg";
			std::string path = front + std::to_string(oscMessage) + back;
			console(path);
			artImage.load(path);
			cameraImage.load("export/export.png");
		}
	}
}

//--------------------------------------------------------------
void ofApp::draw(){
	cameraImage.draw(0, ofGetHeight() / 2, ofGetWidth() / 2, ofGetHeight() / 2);
	artImage.draw(ofGetWidth() / 2, 0, ofGetWidth(), ofGetHeight() / 2);

	console.print(40, 40);
}