
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
	cp servers.json $(CONFIG_DIR)
	cp webServer.py $(BIN_DIR)/home-webServer.py
	cp home-web.service $(SYSTEMD_DIR)
