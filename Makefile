
ifndef $(CONFIG_DIR)
	CONFIG_DIR=/etc/home/
endif

ifndef $(BIN_DIR)
	BIN_DIR=/usr/local/bin/
endif

ifndef $(SYSTEMD_DIR)
	SYSTEMD_DIR=/etc/systemd/system/
endif

install:
	mkdir -p $(CONFIG_DIR)
	mkdir -p $(BIN_DIR)/home-web
	cp servers.json $(CONFIG_DIR)
	cp webServer.py $(BIN_DIR)/home-web/home-webServer.py
	cp -R static $(BIN_DIR)/home-web/
	cp -R templates $(BIN_DIR)/home-web/
	cp home-web.service $(SYSTEMD_DIR)
